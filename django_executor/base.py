from django.core.management import find_commands, load_command_class
from django.utils.encoding import force_str
from django.conf import settings
from django_executor.settings import CONFIG
from cStringIO import StringIO
import os
import sys
import shlex
import traceback


class FunctionOutputWrapper(object):
    def __init__(self, func):
        self.func = func
        self.old_stdout = sys.stdout
        self.old_stderr = sys.stderr
        sys.stdout = self.mystdout = StringIO()
        sys.stderr = self.mystderr = StringIO()
        self.run_method()

    def run_method(self):
        self.func()
        sys.stdout = self.old_stdout
        sys.stderr = self.old_stderr

    def get_stdout_value(self):
        return self.mystdout.getvalue()

    def get_stderr_value(self):
        return self.mystderr.getvalue()


class ManagementExecutor(object):
    def __init__(self, app_name, command_name, argv_raw):
        self.app_name = app_name
        self.command_name = command_name
        self.argv_raw = argv_raw

    def run_with_argv_raw(self, argv_raw):
        try:
            argv = [self.app_name, self.command_name] + shlex.split(argv_raw)
            command_class = load_command_class(self.app_name, self.command_name)
            command_class.run_from_argv(argv)
        except SystemExit:
            pass

    def execute(self):
        try:
            self.run_with_argv_raw(self.argv_raw)
        except Exception, e:
            traceback.print_exc()

    def execute_and_retrieve_std(self):
        wrapper = FunctionOutputWrapper(func=self.execute)
        return wrapper.get_stdout_value(), wrapper.get_stderr_value()


class ManagementUtility(object):
    def find_management_module(self, app_name):
        path = os.path.join(__import__(app_name, fromlist="mangement").__path__[0], "management")
        return path if os.path.exists(path) else None

    def get_app_names(self):
        app_names = []
        for app_name in settings.INSTALLED_APPS:
            if app_name.startswith("django.") and CONFIG.get('HIDE_DJANGO_MANAGEMENT_COMMANDS'):
                continue
            elif app_name in CONFIG.get('EXCLUDED_APPS'):
                continue
            app_names.append(app_name)
        return app_names

    def get_available_options(self, command_class):
        options = []

        for option in command_class.option_list:
            opt_name = option.get_opt_string()
            if opt_name:
                options.append(opt_name)
        return options

    def get_apps_with_commands(self):
        apps = []

        for app_name in self.get_app_names():
            management_module = self.find_management_module(app_name)
            commands = []

            if management_module:
                command_names = find_commands(management_module)
                for command_name in command_names:
                    command = {'command_name': command_name}

                    try:
                        command_class = load_command_class(app_name, command_name)
                        available_options = self.get_available_options(command_class)
                        command.update({
                            'success': True,
                            'message': command_class.help,
                            'available_options': available_options
                        })
                    except Exception, e:
                        command.update({
                            'success': False,
                            'message': force_str(e)
                        })

                    commands.append(command)

            if commands:
                apps.append({'app_name': app_name, 'commands': commands})

        return apps

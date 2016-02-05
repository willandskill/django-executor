from django.views.generic import TemplateView, View
from django.utils import timezone
from django.http import JsonResponse
from django.core.exceptions import PermissionDenied
from django.core import urlresolvers
from base import ManagementUtility, ManagementExecutor
from models import Log


def has_permission(request):
    return request.user.is_authenticated() and request.user.is_superuser


class ManagementCommandListView(TemplateView):
    template_name = 'django_executor/manage-commands.html'

    def get(self, request, *args, **kwargs):
        if not has_permission(request):
            raise PermissionDenied

        utility = ManagementUtility()
        context = self.get_context_data(**kwargs)
        admin_site_url = urlresolvers.reverse("admin:index")
        context.update({'apps': utility.get_apps_with_commands(), 'admin_site_url': admin_site_url})
        return self.render_to_response(context)


class RunManagementCommandView(View):
    def post(self, request, *args, **kwargs):
        if not has_permission(request):
            raise PermissionDenied

        app_name = request.POST.get('appName')
        command_name = request.POST.get('commandName')
        argv_raw = request.POST.get('argvRaw', '')

        started_at = timezone.now()
        executor = ManagementExecutor(app_name=app_name, command_name=command_name, argv_raw=argv_raw)
        stdout, stderr = executor.execute_and_retrieve_std()
        ended_at = timezone.now()

        Log.objects.create(
            user=request.user,
            app_name=app_name,
            command_name=command_name,
            argv_raw=argv_raw,
            stdout=stdout,
            stderr=stderr,
            started_at=started_at,
            ended_at=ended_at
        )

        return JsonResponse({'stdout': stdout, 'stderr': stderr})

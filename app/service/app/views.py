from django.views.generic import TemplateView
from django.views.generic import DetailView
from django.shortcuts import get_object_or_404
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.shortcuts import redirect

from service.groupinformation.models import HomeInfo
from service.groupinformation.models import ProjectInfo
from service.groupinformation.models import ResearchLine
from service.groupinformation.models import Repository
from service.groupinformation.models import CourseInfo
from service.groupinformation.models import EventInfo
from service.groupinformation.models import Gallery
from service.groupinformation.models import Image
from service.groupinformation.models import Scholarship
from service.members.models import Member
from service.members.models import Publication
from service.app.forms import ContactForm


class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['home_info'] = HomeInfo.objects.all()
        return context


class PhdthesisView(TemplateView):
    template_name = 'phdthesis.html'


class StaffMembersView(TemplateView):
    template_name = 'members_staff.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['members'] = Member.objects.all()
        return context


class AllSdasersView(TemplateView):
    template_name = 'members_all.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['members'] = Member.objects.all()
        return context


class StudentMembersView(TemplateView):
    template_name = 'members_students.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['members'] = Member.objects.all()
        return context


class SingleMemberView(DetailView):
    Model = Member
    context_object_name = 'single_member'
    template_name = 'single-member.html'

    def get_object(self):
        single_member = get_object_or_404(
            Member,
            slug=self.kwargs['slug'],
        )
        return single_member

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        Single_Member = self.get_object()
        context['Publications'] = Publication.objects.filter(
            member__full_name=Single_Member.full_name).order_by(
            'year', 'id').reverse()

        return context


class VolunteerMemberView(TemplateView):
    template_name = 'members_volunteer.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['members'] = Member.objects.all()
        return context


class HonoraryMemberView(TemplateView):
    template_name = 'members_honorary.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['members'] = Member.objects.all()
        return context


class ResearchBoardView(TemplateView):
    template_name = 'research-board.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['members'] = Member.objects.all()
        return context


class ExternalMemberView(TemplateView):
    template_name = 'members_external.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['members'] = Member.objects.all()
        return context


class ProjectsView(TemplateView):
    template_name = 'projects.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['project_info'] = ProjectInfo.objects.all().order_by(
            'id').reverse()
        return context


class SingleProjectView(DetailView):
    Model = ProjectInfo
    template_name = 'single-project.html'
    context_object_name = 'single_project'

    def get_object(self):
        single_project = get_object_or_404(
            ProjectInfo, id=self.kwargs.get('pk'),
        )
        return single_project


class ServicesView(TemplateView):
    template_name = 'services.html'


class ResearchLineView(TemplateView):
    template_name = 'research-lines.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['research_line_info'] = ResearchLine.objects.all()
        return context


class RepositoriesView(TemplateView):
    template_name = 'repositories.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['repositories'] = Repository.objects.all()
        return context


class MaterialView(TemplateView):
    template_name = 'material.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['repositories'] = Repository.objects.all()
        return context


class ContactFormView(TemplateView):
    template_name = 'contact_form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['contact_form'] = ContactForm()

        return context

    def post(self, request, *args, **kwargs):
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        message = request.POST.get('message')

        body = render_to_string(
            'contact_form_message.html', {
                'name': name,
                'email': email,
                'phone': phone,
                'message': message,
            },
        )

        email_message = EmailMessage(
            subject='Web User Message',
            body=body,
            from_email=email,
            to=[
                'contact@sdas-group.com',
            ],
        )

        email_message.content_subtype = 'html'
        email_message.send()

        return redirect('contact_success')


class GalleryView(TemplateView):
    template_name = 'gallery.html'


class SingleGalleryView(DetailView):
    Model = Image
    context_object_name = 'title_gallery'
    template_name = 'single-gallery.html'

    def get_object(self):
        gallery = get_object_or_404(Gallery, slug=self.kwargs['slug'])
        return gallery

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        gallery = self.get_object()
        context['images'] = Image.objects.filter(
            album__slug=gallery.slug
        )

        context['title_gallery'] = gallery.title
        return context


class ContactSuccessView(TemplateView):
    template_name = 'contact_success.html'


class ContactView(TemplateView):
    template_name = 'contact.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['contact_form'] = ContactForm()

        return context

    def post(self, request, *args, **kwargs):
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        message = request.POST.get('message')

        body = render_to_string(
            'contact_form_message.html', {
                'name': name,
                'email': email,
                'phone': phone,
                'message': message,
            },
        )

        email_message = EmailMessage(
            subject='Web User Message',
            body=body,
            from_email=email,
            to=[
                'contact@sdas-group.com',
            ],
        )

        email_message.content_subtype = 'html'
        email_message.send()

        return redirect('contact_success')


class CoursesView(TemplateView):
    template_name = 'courses.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['courses'] = CourseInfo.objects.all().order_by(
            'id').reverse()
        return context


class DocumentationView(TemplateView):
    template_name = 'documentation.html'


class ScholarshipsView(TemplateView):
    template_name = 'scholarships.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['scholarships'] = Scholarship.objects.all().order_by(
            'id').reverse()
        return context


class OurPublicationsView(TemplateView):
    template_name = 'all_publications.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Publications'] = Publication.objects.filter(
            member__id=1,
        ).order_by('year', 'id').reverse()

        return context


class EventsView(TemplateView):
    template_name = 'events.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['events'] = EventInfo.objects.all()
        return context


class OurAreasView(TemplateView):
    template_name = 'research-topics.html'


class TermsofuseView(TemplateView):
    template_name = 'terms_of_use.html'


class AboutView(TemplateView):
    template_name = 'about.html'


class ManifiestoView(TemplateView):
    template_name = 'manifiesto.html'


class CallProjectsView(TemplateView):
    template_name = 'call-for-projects.html'


class MachineLearningView(TemplateView):
    template_name = 'machine_learning_and_data_analytics.html'


class AppliedMathematicsView(TemplateView):
    template_name = 'applied_mathematics.html'


class IntelligentEmbeddedSystemsView(TemplateView):
    template_name = 'intelligent_embedded_systems.html'


class ArtificialIntelligenceView(TemplateView):
    template_name = 'artificial_intelligence.html'


class ComputerVisionView(TemplateView):
    template_name = 'computer_vision.html'


class DeepLearningView(TemplateView):
    template_name = 'deep_learning.html'


class DigitalSignalProcessingView(TemplateView):
    template_name = 'digital_signal_processing.html'


class HumanMachineInteractionView(TemplateView):
    template_name = 'human-machine_interaction.html'


class MedicalDataAnalysisView(TemplateView):
    template_name = 'medical_data_analysis.html'


class SoftwareEngineeringView(TemplateView):
    template_name = 'software_engineering.html'

class ResearchEngineersView(TemplateView):
    template_name = 'research_engineers.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['members'] = Member.objects.all()
        return context

class PartnershipView(TemplateView):
    template_name = 'partnership.html'

class CendecytView(TemplateView):
    template_name = 'cendecyt.html'

from django.conf import settings
from django.conf.urls import url
from django.conf.urls import include
from django.contrib import admin

from service.app.views import HomeView
from service.app.views import SingleMemberView
from service.app.views import ProjectsView
from service.app.views import SingleProjectView
from service.app.views import ServicesView
from service.app.views import RepositoriesView
from service.app.views import MaterialView
from service.app.views import ContactView
from service.app.views import ContactSuccessView
from service.app.views import CoursesView
from service.app.views import EventsView
from service.app.views import StaffMembersView
from service.app.views import StudentMembersView
from service.app.views import AssociateMemberView
from service.app.views import PrincipalMemberView
from service.app.views import PhdMemberView
from service.app.views import MasterMemberView
from service.app.views import VolunteerMemberView
from service.app.views import FormerMembersView
from service.app.views import ExternalMemberView
from service.app.views import GalleryView
from service.app.views import SingleGalleryView
from service.app.views import DocumentationView
from service.app.views import AllPublicationsView
from service.app.views import ResearchTopicsView
from service.app.views import HonoraryMemberView
from service.app.views import TermsofuseView
from service.app.views import AboutView
from service.app.views import ScholarshipsView
from service.app.views import ContactFormView
from service.app.views import ResearchBoardView
from service.app.views import ManifiestoView
from service.app.views import CallProjectsView
from service.app.views import MachineLearningView
from service.app.views import AppliedMathematicsView
from service.app.views import IntelligentEmbeddedSystemsView
from service.app.views import ArtificialIntelligenceView
from service.app.views import ComputerVisionView
from service.app.views import DeepLearningView
from service.app.views import DigitalSignalProcessingView
from service.app.views import HumanMachineInteractionView
from service.app.views import MedicalDataAnalysisView
from service.app.views import SoftwareEngineeringView
from service.app.views import ResearchEngineersView

admin.site.site_title = 'SDAS Group'
admin.site.site_header = 'SDAS Group - Administrator'

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(
        r'^about/$',
        AboutView.as_view(),
        name='about',
    ),

    url(
        r'^$',
        HomeView.as_view(),
        name='home',
    ),

    url(
        r'^members-staff/$',
        StaffMembersView.as_view(),
        name='members_staff',
    ),

    url(
        r'^members-students/$',
        StudentMembersView.as_view(),
        name='members_students',
    ),

    url(
        r'^associate/$',
        AssociateMemberView.as_view(),
        name='associate_members',
    ),

    url(
        r'^principal/$',
        PrincipalMemberView.as_view(),
        name='principal_members',
    ),

    url(
        r'^phd/$',
        PhdMemberView.as_view(),
        name='phd_members',
    ),

    url(
        r'^master/$',
        MasterMemberView.as_view(),
        name='master_members',
    ),

    url(
        r'^volunteer/$',
        VolunteerMemberView.as_view(),
        name='volunteer_members',
    ),

    url(
        r'^former-members/$',
        FormerMembersView.as_view(),
        name='former_members',
    ),

    url(
        r'^members/(?P<slug>[\w-]+)/$',
        SingleMemberView.as_view(),
        name='single_member',
    ),

    url(
        r'^honorary-member/$',
        HonoraryMemberView.as_view(),
        name='members_honorary',
    ),

    url(
        r'^external-member/$',
        ExternalMemberView.as_view(),
        name='external_members',
    ),

    url(
        r'^projects/$',
        ProjectsView.as_view(),
        name='projects',
    ),

    url(
        r'^projects/(?P<pk>\d+)/$',
        SingleProjectView.as_view(),
        name='single_project',
    ),

    url(
        r'^services/$',
        ServicesView.as_view(),
        name='services',
    ),

    url(
        r'^gallery/$',
        GalleryView.as_view(),
        name='gallery',
    ),

    url(
        r'^gallery/(?P<slug>[\w-]+)/$',
        SingleGalleryView.as_view(),
        name='single-gallery',
    ),

    url(
        r'^repositories/$',
        RepositoriesView.as_view(),
        name='repositories',
    ),

    url(
        r'^material/$',
        MaterialView.as_view(),
        name='material',
    ),

    url(
        r'^contact-success/$',
        ContactSuccessView.as_view(),
        name='contact_success',
    ),

    url(
        r'^contact/$',
        ContactView.as_view(),
        name='contact',
    ),

    url(
        r'^courses/$',
        CoursesView.as_view(),
        name='courses',
    ),

    url(
        r'^events/$',
        EventsView.as_view(),
        name='events',
    ),

    url(
        r'^documentation/$',
        DocumentationView.as_view(),
        name='documentation',
    ),

    url(
        r'^termsofuse/$',
        TermsofuseView.as_view(),
        name='termsofuse',
    ),

    url(
        r'^scholarships/$',
        ScholarshipsView.as_view(),
        name='scholarships',
    ),

    url(
        r'^allpublications/$',
        AllPublicationsView.as_view(),
        name='allpublications',
    ),

    url(
        r'^researchtopics/$',
        ResearchTopicsView.as_view(),
        name='research_topics',
    ),

    url(
        r'^contactform/$',
        ContactFormView.as_view(),
        name='contact_form',
    ),

    url(
        r'^manifesto/$',
        ManifiestoView.as_view(),
        name='manifiesto',
    ),

    url(
        r'^research-board/$',
        ResearchBoardView.as_view(),
        name='research_board',
    ),

    url(
        r'^call-for-projects/$',
        CallProjectsView.as_view(),
        name='call_for_projects',
    ),

    url(
        r'^machine-learning/$',
        MachineLearningView.as_view(),
        name='machine_learning',
    ),

    url(
        r'^applied-mathematics/$',
        AppliedMathematicsView.as_view(),
        name='applied_mathematics',
    ),

    url(
        r'^intelligent-embedded-systems/$',
        IntelligentEmbeddedSystemsView.as_view(),
        name='intelligent_embedded_systems',
    ),

    url(
        r'^artificial-intelligence/$',
        ArtificialIntelligenceView.as_view(),
        name='artificial_intelligence',
    ),

    url(
        r'^computer-vision/$',
        ComputerVisionView.as_view(),
        name='computer_vision',
    ),

    url(
        r'^deep-learning/$',
        DeepLearningView.as_view(),
        name='deep_learning',
    ),

    url(
        r'^digital-signal-processing/$',
        DigitalSignalProcessingView.as_view(),
        name='digital_signal_processing',
    ),


    url(
        r'^human-machine-interaction/$',
        HumanMachineInteractionView.as_view(),
        name='human-machine-interaction',
    ),


    url(
        r'^medical-data-analysis/$',
        MedicalDataAnalysisView.as_view(),
        name='medical_data_analysis',
    ),


    url(
        r'^software-engineering/$',
        SoftwareEngineeringView.as_view(),
        name='software_engineering',
    ),

    url(
        r'^research_engineers/$',
        ResearchEngineersView.as_view(),
        name='research_engineers',
    ),
]


if settings.DEBUG:
    from django.conf.urls.static import static
    import debug_toolbar

    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns

    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )

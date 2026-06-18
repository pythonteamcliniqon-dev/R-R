from django.urls import path

from . import views

urlpatterns = [
    path("first_page_list/", views.first_page_list, name="first_page_list"),
    path("next-page/", views.next_page_dashboard, name="next_page_dashboard"),
    path("next-page-view/", views.next_page_view, name="next_page_view"),
    path("agency-page/", views.agency_page_dashboard, name="agency_page_dashboard"),
    path("agency-page-view/", views.agency_page_view, name="agency_page_view"),
    path("bullet-page/", views.bullet_page_dashboard, name="bullet_page_dashboard"),
    path("bullet-page-view/", views.bullet_page_view, name="bullet_page_view"),
    path("client-date-page/", views.client_date_page_dashboard, name="client_date_page_dashboard"),
    path("client-date-page-view/", views.client_date_page_view, name="client_date_page_view"),
    path("client-says-page/", views.client_says_page_dashboard, name="client_says_page_dashboard"),
    path("client-says-page-view/", views.client_says_page_view, name="client_says_page_view"),
    path("gallery-page/", views.gallery_page_dashboard, name="gallery_page_dashboard"),
    path("gallery-page-view/", views.gallery_page_view, name="gallery_page_view"),
    path("new-joiners/", views.new_joiners_dashboard, name="new_joiners_dashboard"),
    path("new-joiners-view/", views.new_joiners_view, name="new_joiners_view"),
    path("promotions/", views.promotions_dashboard, name="promotions_dashboard"),
    path("promotions-view/", views.promotions_view, name="promotions_view"),
    path("kudos-moments/", views.kudos_moments_dashboard, name="kudos_moments_dashboard"),
    path("kudos-moments-view/", views.kudos_moments_view, name="kudos_moments_view"),
    path("kudos-bullet-moments/", views.kudos_bullet_moments_dashboard, name="kudos_bullet_moments_dashboard"),
    path("kudos-bullet-moments-view/", views.kudos_bullet_moments_view, name="kudos_bullet_moments_view"),
    path("special-appreciation/", views.special_appreciation_dashboard, name="special_appreciation_dashboard"),
    path("special-appreciation-view/", views.special_appreciation_view, name="special_appreciation_view"),
    path("caption-slide-page/", views.caption_slide_page_dashboard, name="caption_slide_page_dashboard"),
    path("caption-slide-page-view/", views.caption_slide_page_view, name="caption_slide_page_view"),
    path("", views.dashboard, name="dashboard"),
]

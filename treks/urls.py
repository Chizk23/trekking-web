# treks/urls.py

from django.urls import path
from . import user_views

# app_name là bắt buộc để Django nhận diện được namespace
app_name = 'treks'

urlpatterns = [
    # === DANH SÁCH CUNG ĐƯỜNG ===
    path('', user_views.CungDuongListView.as_view(), name='cung_duong_list'),
    
    # === USER CONTRIBUTION ROUTES (ĐẶT TRƯỚC <slug:slug> ĐỂ TRÁNH CONFLICT) ===
    path('dong-gop/', user_views.UserTrekContributeView.as_view(), name='contribute_trek'),
    path('cua-toi/', user_views.MyTreksListView.as_view(), name='my_treks'),
    path('cua-toi/<int:pk>/chinh-sua/', user_views.UserTrekUpdateView.as_view(), name='my_trek_update'),
    path('cua-toi/<int:pk>/xoa/', user_views.UserTrekDeleteView.as_view(), name='my_trek_delete'),
    
    # === REVIEW ROUTES ===
    path('review/<int:pk>/delete/', user_views.delete_review, name='delete_review'),
    path('api/review/<int:pk>/', user_views.get_review_data, name='get_review_data'),
    path('api/review-image/<int:pk>/delete/', user_views.delete_review_image, name='delete_review_image'),
    
    # === DETAIL VIEW (ĐẶT CUỐI CÙNG VÌ BẮT MỌI SLUG) ===
    path('<slug:slug>/', user_views.CungDuongDetailView.as_view(), name='cung_duong_detail'),
]
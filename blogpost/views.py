from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions  import IsAuthenticated, AllowAny
from rest_framework_simplejwt.authentication import JWTAuthentication 
from .pagination import MyPageNumberPagination
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from django.db.models import Q
from rest_framework import status
from .serializers import *


@api_view(["POST"])
@permission_classes([IsAuthenticated])
@authentication_classes([JWTAuthentication])
def create_category(request):
    serializers = CategorySerializers(data=request.data)
    serializers.is_valid(raise_exception=True)
    serializers.save()
    return Response(serializers.data, status=status.HTTP_201_CREATED)



@api_view(["POST"])
@permission_classes([IsAuthenticated])
@authentication_classes([JWTAuthentication])
def create_post(request):
    serializers = PostCreateSerializers(data=request.data)
    serializers.is_valid(raise_exception=True)
    serializers.save(author=request.user)
    return Response(serializers.data, status=status.HTTP_201_CREATED)

@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
@authentication_classes([JWTAuthentication])
def post_update(request, id):
    post = get_object_or_404(Post, id=id, author=request.user)
    serializers = PostUpdateSerializers(post, data=request.data, partial=True)
    serializers.is_valid(raise_exception=True)
    serializers.save()
    return Response(serializers.data, status=status.HTTP_200_OK)


@api_view(["DELETE"])
@permission_classes([IsAuthenticated])
@authentication_classes([JWTAuthentication])
def delete_post(request, id):
    delete_post = get_object_or_404(Post, id=id, author=request.user)
    delete_post.delete()
    return Response({"message": "post delete successful."}, status=status.HTTP_200_OK)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
@authentication_classes([JWTAuthentication])
def user_post(request):
    post = Post.objects.filter(author=request.user)
    serializers = PostCreateSerializers(post, many=True)
    return Response(serializers.data, status=status.HTTP_200_OK)

@api_view(["GET"])
@permission_classes([AllowAny])
def read_post(request):
    post = Post.objects.all()
    pagination = MyPageNumberPagination()
    paginated_post =  pagination.paginate_queryset(post, request)
    serializers = PostCreateSerializers(paginated_post, many=True)
    return pagination.get_paginated_response(serializers.data)


@api_view(["GET"])
@permission_classes([AllowAny])
def search(request):
    query = request.GET.get("q")
    if not query:
        return Response({"message": "query missing"}, status=status.HTTP_400_BAD_REQUEST)
    search_post = Post.objects.filter(
        Q(title__icontains=query)| 
        Q(category__name__icontains=query)
    )
    if not search_post.exists():
        return Response({"message": "not found"}, status=status.HTTP_404_NOT_FOUND)
    serializers = PostCreateSerializers(search_post, many=True)
    return Response(serializers.data, status=status.HTTP_200_OK)

@api_view(["POST"])
@permission_classes([IsAuthenticated])
@authentication_classes([JWTAuthentication])
def comment(request, post_id):
    data = request.data.copy()
    data['post'] = post_id
    data['user'] = request.user.id
    serializers = CommentSerializers(data=data)
    serializers.is_valid(raise_exception=True)
    serializers.save(user=request.user, post_id=post_id)
    return Response(serializers.data, status=status.HTTP_201_CREATED)


@api_view(["PATCH"])
@permission_classes([IsAuthenticated])
@authentication_classes([JWTAuthentication])
def comment_edit(request, id):
    comment = get_object_or_404(Comment, id=id,  user=request.user)
    serializers = CommentUpdateSerializers(comment, data=request.data, partial=True)
    serializers.is_valid(raise_exception=True)
    serializers.save()
    return Response(serializers.data, status=status.HTTP_200_OK)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
@authentication_classes([JWTAuthentication])
def comment_read(request, post_id):
    comment = Comment.objects.filter(post_id=post_id)
    serializers = CommentSerializers(comment, many=True)
    return Response(serializers.data, status=status.HTTP_200_OK)
    


@api_view(["DELETE"])
@permission_classes([IsAuthenticated])
@authentication_classes([JWTAuthentication])
def comment_delete(request, id):
    comment = get_object_or_404(Comment, id=id, user=request.user)
    comment.delete()
    return Response({"message": "Comment delete successful."}, status=status.HTTP_200_OK)





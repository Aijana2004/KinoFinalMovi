#from rest_framework  import serializers
#from .models import *
from rest_framework import generics, status, viewsets, permissions
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken
from django.http import HttpResponseRedirect
from django.urls import reverse
from .serializers import *
from .models import models




class RegisterView(generics.CreateAPIView):
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token = RefreshToken.for_user(user)
        return Response({
            'user': {
                'email': user.email,
                'username': user.username,
                'token': str(token.access_token),

            }
        }, status=status.HTTP_201_CREATED)


class CustomLoginView(TokenObtainPairView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
        except Exception:
            return Response({"detail": "Неверные учетные данные"}, status=status.HTTP_401_UNAUTHORIZED)

        user = serializer.validated_data
        refresh = RefreshToken.for_user(user)
        response = HttpResponseRedirect(reverse('product_list'))
        response.set_cookie('token', str(refresh.access_token))
        return response


class LogoutView(generics.GenericAPIView):
    def post(self, request, *args, **kwargs):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer



class ProductPhotosViewSet(viewsets.ModelViewSet):
    queryset = ProductPhotos.objects.all()
    serializer_class = ProductPhotosSerializer


class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'



class UserProfileSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['first_name','last_name']



class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'







class ProductPhotosSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductPhotos
        fields = '__all__'



class RatingSerializer(serializers.ModelSerializer):
    user= UserProfileSimpleSerializer()
    class Meta:
        model = Rating
        fields = '__all__'




class ReviewSerializer(serializers.ModelSerializer):
    author = UserProfileSimpleSerializer()
    created_date = serializers.DateTimeField(format('%d-%m-%Y %H:%M'))
    class Meta:
        model = Review
        fields = '__all__'




class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    ratings = RatingSerializer(many=True,read_only= True)
    reviews = ReviewSerializer(many=True,read_only=True)
    product = ProductPhotosSerializer(many=True,read_only=True)
    date = serializers.DateTimeField(format('%d-%m-%Y'))

    class Meta:
        model = Product
        fields = [ 'product_name', 'category','price','product','description','date',
                   'active','product_video','ratings','reviews']



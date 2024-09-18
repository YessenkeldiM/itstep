from .models import Good, Magazin
from .serializers import GoodSerializer, MagazinSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework.permissions import IsAuthenticated

# @api_view(['GET', 'POST'])
# def api_goods(request):
#     if request.method == 'GET':
#         goods = Good.objects.all()
#         serializer = GoodSerializer(goods, many=True)
#         return Response(serializer.data)
#     if request.method == 'POST':
#         serializer = GoodSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)



# @api_view(['GET', 'PUT', 'DELETE', 'PATCH'])
# def api_good_detail(request, pk):
#     good = Good.objects.get(pk=pk)
#     if request.method == 'GET':
#         serializer = GoodSerializer(good)
#         return Response(serializer.data)
#     elif request.method == 'PUT' or request.method == 'PATCH':
#         serializer = GoodSerializer(good, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#     elif request.method == 'DELETE':
#         good.delete()
#         return Response('Success delete',status=status.HTTP_204_NO_CONTENT)
#     return Response(status=status.HTTP_400_BAD_REQUEST)


# class APIGoods(generics.ListCreateAPIView):
#     queryset = Good.objects.all()
#     serializer_class = GoodSerializer


# class APIGoodsDetail(generics.RetrieveUpdateDestroyAPIView):
    # queryset = Good.objects.all()
    # serializer_class = GoodSerializer


@permission_classes((IsAuthenticated, ))
class APIGoodsViewSet(ModelViewSet):
    queryset = Good.objects.all()
    serializer_class = GoodSerializer
    

class APIReadonlyMagazinViewSet(ReadOnlyModelViewSet):
    queryset = Magazin.objects.all()
    serializer_class = MagazinSerializer
    permission_classes = (IsAuthenticated, )
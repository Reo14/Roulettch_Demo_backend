from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Memo
from .serializers import MemoSerializer

@api_view(['GET', 'POST'])
def memo_list(request):
    if request.method == 'GET':
        memos = Memo.objects.all()
        serializer = MemoSerializer(memos, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = MemoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def memo_detail(request, pk):
    try:
        memo = Memo.objects.get(pk=pk)
    except Memo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        memo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

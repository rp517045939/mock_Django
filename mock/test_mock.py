from django.http import JsonResponse
from django.core.exceptions import ValidationError


# 添加mock接口
def add_advance(request):
    id_num = request.POST.get('id_num', '')
    if id_num == '':
        return JsonResponse({'status': 9999, 'message': 'data err'})
    else:
        return JsonResponse({'status': 200, 'message': 'OK' + id_num})


# 添加mockadvance的

def mock_advance(request):
    advance = request.POST.get('advance', '')
    faceImage = request.POST.get('faceImage', '')
    referId = request.POST.get('referId', '')
    idNumber = request.POST.get('idNumber', '')
    imageType = request.POST.get('', '')
    if advance is '':
        return JsonResponse({
            "code": "SUCCESS",
            "transactionId": "196eb0c777789e58",
            "pricingStrategy": "PAY",
            "message": "OK",
            "data": {
                "result": [
                    {
                        "referId": "332090",
                        "idNumber": "371821330",
                        "similarity": 89.12374387
                    },
                    {
                        "referId": "332091",
                        "idNumber": "371821334",
                        "similarity": 88.928037477
                    }
                ],
                "imageId": "FACE_SEARCH-eb6ce0ae6b33a6b6_20190107144540742_9103533175.jpg"
            }

        })
    else:
        return JsonResponse({
            "code": "SUCCESS",
            "transactionId": advance,
            "pricingStrategy": "PAY",
            "message": "OK",
            "data": {}

        })


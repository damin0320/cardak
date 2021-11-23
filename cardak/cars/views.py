import json
from json import JSONDecodeError

from django.views import View
from django.http  import JsonResponse
from django.db        import IntegrityError
from django.db.utils  import DataError

from .models import Car

from users.models  import Users

from utils.decorators import auth_check

class CarRegistryView(View):
    @auth_check
    def post(self, request):
        try:
            data = json.loads(request.body)

            brand_name = data['brand_name']
            country = data['country']
            model_name = data['model_name']
            year_type = data['year_type']
            trim_id = data['trim_id']
            price = data['price']
            user = request.user

            Car.objects.create(
                brand_name = brand_name,
                country = country,
                model_name = model_name,
                year_type = year_type,
                trim_id = trim_id,
                price = price,
                user = user
            )
            return JsonResponse({'message' : 'SUCCESS'}, status=200)

        except KeyError:
            return JsonResponse({'message': 'KEY_ERROR'}, status=400)
        except JSONDecodeError:
            return JsonResponse({'message': 'JSON_DECODE_ERROR'}, status=400)
        except IntegrityError:
            return JsonResponse({'message': 'INTEGRITY_ERROR'}, status=400)
        except DataError:
            return JsonResponse({'message': 'DATA_ERROR'}, status=400)
        except TypeError:
            return JsonResponse({'message': 'TYPE_ERROR'}, status=400)
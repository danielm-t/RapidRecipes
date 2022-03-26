from django.http import JsonResponse
from food.models import Measurement, RawFood
# Create your views here.

def getRawFoodMeasurementTypes(request):
    if request.is_ajax and request.method == "GET":
        rawFood = request.GET.get("raw-food", None)
        response={}
        try:
            rawFoodInstance = RawFood.objects.get(name = rawFood)
            measurementTypes = rawFoodInstance.measuredIn.all()
            for idx, measurement in enumerate(measurementTypes):
                response[idx] = measurement.unit
        except (RawFood.DoesNotExist, Measurement.DoesNotExist) as e:
            return JsonResponse({}, status=400)
        return JsonResponse(response, status=200)
    return JsonResponse({}, status=400)

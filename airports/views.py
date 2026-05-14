from django.http import JsonResponse
from django.views import View
from django.db.models import Q

from .models import Airport


class AirportListView(View):

    def get(self, request):
        
        queryset = Airport.objects.filter(is_active=True)

        search = request.GET.get('search')
        country = request.GET.get('country')
        city = request.GET.get('city')
        airport_type = request.GET.get('airport_type')

        if search:
            search = search.strip()

            if len(search) < 2:
                return JsonResponse(
                    {
                        "succes": False,
                        "message": "Search must contain at least 2 characters."
                    },
                    status = 400
                )

            queryset = queryset.filter(
                Q(name__icontains=search)
                | Q(city__icontains=search)
                | Q(country__icontains=search)
                | Q(airport_code__icontains=search)
                | Q(icao_code__icontains=search)
                | Q(city_code__icontains=search)
                | Q(country_code__icontains=search)
            )

        if country:
            queryset = queryset.filter(
                country__icontains=country.strip()
            )

        if city:
            queryset = queryset.filter(
                city__icontains=city.strip()
            )
        
        if airport_type:
            valid_types = [choice[0] for choice in Airport.AirportType.choices]

            if airport_type not in valid_types:
                return JsonResponse(
                    {
                        "success": False,
                        "message": "Invalid airport_type",
                        "allowed": valid_types
                    }
                )
            
            queryset = queryset.filter(
                airport_type=airport_type
            )

        queryset = queryset.distinct()

        data = list(
            queryset.values(
                "id",
                "airport_code",
                "icao_code",
                "name",
                "slug",
                "city",
                "city_code",
                "country",
                "country_code",
                "airport_type",
                "timezone",
            )
        )

        return JsonResponse(
            {
                "success": True,
                "count": len(data),
                "results": data
            },
            safe=False
        )
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from django.db.models import Sum
from .models import RegistroDeHoras
from .serializers import RegistroDeHorasSerializer
from django.utils.dateparse import parse_date
from datetime import datetime, timedelta

class RegistroDeHorasViewSet(viewsets.ModelViewSet):
    serializer_class = RegistroDeHorasSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = None  # Deshabilitamos paginación para este ViewSet

    def get_queryset(self):
        return RegistroDeHoras.objects.filter(usuario=self.request.user).order_by('-fecha')

    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)

    # Endpoint extra para resumen semanal
    def resumen_semanal(self, request):
        fecha_str = request.query_params.get('fecha')
        if fecha_str:
            try:
                fecha_ref = parse_date(fecha_str)
                if fecha_ref is None:
                    raise ValueError()
            except:
                return Response({'error': 'Formato de fecha inválido (YYYY-MM-DD esperado)'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            fecha_ref = datetime.today().date()

        inicio_semana = fecha_ref - timedelta(days=fecha_ref.weekday())
        fin_semana = inicio_semana + timedelta(days=6)

        registros = RegistroDeHoras.objects.filter(
            usuario=request.user,
            fecha__range=(inicio_semana, fin_semana)
        )

        total_horas = registros.aggregate(Sum('horas'))['horas__sum'] or 0
        horas_extra = total_horas - 24 if total_horas > 24 else 0

        return Response({
            'inicio_semana': inicio_semana,
            'fin_semana': fin_semana,
            'total_horas': total_horas,
            'horas_extra': horas_extra,
        })

 

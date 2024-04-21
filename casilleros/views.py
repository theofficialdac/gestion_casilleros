
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Casillero, Contrato
from .serializers import CasilleroSerializer, ContratoSerializer, CustomUserSerializer
from django.shortcuts import render

from django.core.mail import send_mail
from django.http import HttpResponseRedirect

from django.shortcuts import render, redirect
from django.contrib import messages

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from casilleros.models import Casillero
from casilleros.serializers import CasilleroSerializer, ContratoSerializer


def index(request):
    if request.method == 'POST':
        # Extraer la información del formulario
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Construir el mensaje de correo electrónico
        subject = f'Nuevo mensaje de contacto de {name}'
        message = f'Mensaje: {message}\nDe: {name}\nEmail: {email}'
        email_from = email  # Email del remitente
        recipient_list = ['ramauchile@ieee.org',]  # Email del destinatario

        # Enviar el correo electrónico
        send_mail(subject, message, email_from, recipient_list)

        # Agregar un mensaje de éxito que se mostrará en la plantilla
        messages.success(request, 'Gracias por contactarnos. ¡Responderemos pronto!')

        # Redirigir a la misma página para mostrar la confirmación
        return redirect('index')

    # Si no es un POST, simplemente renderizamos la página
    return render(request, 'casilleros/index.html')

def send_contact_email(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Aquí iría la lógica para enviar el correo electrónico
        send_mail(
            '[IEEE WebPage] Contacto de: ' + name,
            message,
            email,
            ['ramauchile@ieee.org'],  # El correo electrónico donde quieres recibir los mensajes
            fail_silently=False,
        )

        messages.success(request, 'Gracias por contactarnos. ¡Responderemos pronto!')
        return redirect('index')

    return render(request, 'contact.html', {})


class CasilleroList(APIView):
    """
    List all lockers, or create a new locker.
    """
    def get(self, request, format=None):
        casilleros = Casillero.objects.all()
        serializer = CasilleroSerializer(casilleros, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CasilleroSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ContratoCreate(APIView):
    def post(self, request, format=None):
        serializer = ContratoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ContratoUpdate(APIView):
    def put(self, request, id, format=None):
    	try:
            contrato = Contrato.objects.get(pk=id)
            serializer = ContratoSerializer(contrato, data=request.data)
            if serializer.is_valid():
               serializer.save()
               return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    	except Contrato.DoesNotExist:
            return Response({"error": "Contrato no encontrado"}, status=status.HTTP_404_NOT_FOUND)

class ContratoList(APIView):
    def get(self, request, format=None):
        contratos = Contrato.objects.all()
        serializer = ContratoSerializer(contratos, many=True)
        return Response(serializer.data)

class ContratoDetail(APIView):
    def get(self, request, id, format=None):
        try:
            contrato = Contrato.objects.get(pk=id)
            serializer = ContratoSerializer(contrato)
            return Response(serializer.data)
        except Contrato.DoesNotExist:
            return Response({"error": "Contrato no encontrado"}, status=status.HTTP_404_NOT_FOUND)



class UserCreate(APIView):
    def post(self, request, format=None):
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


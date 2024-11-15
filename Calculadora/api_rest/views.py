from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from django.contrib.auth.models import User


class ProtectedView():    
    permission_classes = [IsAuthenticated]

    @api_view(['GET'])
    def get(self, operador, numero_um, numero_dois):

        try:
            numero_um = int(numero_um)
            numero_dois = int(numero_dois)
        except ValueError:
            return HttpResponse("Erro: Os números precisam ser valores válidos.", status=400)
        
        if operador.lower() not in ('somar', 'subtrair','multiplicar', 'dividir'):
            return Response({"error":
                                     "o operador deve ser: somar, subtrair, multiplicar ou dividir."
                                     },
                                    status=status.HTTP_400_BAD_REQUEST)
        
        resutado = 0
        calculo_final = ""
        if operador.lower() == 'somar':
            resutado = numero_um + numero_dois
            calculo_final = str(numero_um)+" + "+str(numero_dois)+" = "+ str(resutado)
        elif  operador.lower() == 'subtrair':
            resutado = numero_um - numero_dois
            calculo_final = str(numero_um)+" - "+str(numero_dois)+" = "+ str(resutado)
        elif operador.lower() == 'multiplicar':
            resutado = numero_um * numero_dois
            calculo_final = str(numero_um)+" * "+str(numero_dois)+" = "+ str(resutado)
        elif  operador.lower() == 'dividir':
            resutado = numero_um / numero_dois
            calculo_final = str(numero_um)+" ÷ "+str(numero_dois)+" = "+ str(resutado)

        json_calculo = {}
        json_calculo["result"] = calculo_final
        
        return Response(json_calculo)
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

import uuid

# Simulación de base de datos local en memoria
data_list = []

# Añadiendo algunos datos de ejemplo para probar el GET
data_list.append({'id': str(uuid.uuid4()), 'name': 'User01', 'email': 'user01@example.com', 'is_active': True})
data_list.append({'id': str(uuid.uuid4()), 'name': 'User02', 'email': 'user02@example.com', 'is_active': True})
data_list.append({'id': str(uuid.uuid4()), 'name': 'User03', 'email': 'user03@example.com', 'is_active': False})  # Ejemplo de item inactivo

class DemoRestApi(APIView):
    name = "Demo REST API"

    def get(self, request):
        active_items = [item for item in data_list if item.get("is_active", False)]
        return Response(active_items, status=status.HTTP_200_OK)

    def post(self, request):
        data = request.data

        if 'name' not in data or 'email' not in data:
            return Response(
                {'error': 'Faltan campos requeridos: name y email.'},
                status=status.HTTP_400_BAD_REQUEST,
            )

        data['id'] = str(uuid.uuid4())
        data['is_active'] = True
        data_list.append(data)

        return Response(
            {'message': 'Dato guardado exitosamente.', 'data': data},
            status=status.HTTP_201_CREATED,
        )


class DemoRestApiItem(APIView):
    def get_item(self, id):
        return next((item for item in data_list if item.get('id') == id), None)

    def put(self, request, id):
        item = self.get_item(id)
        if item is None:
            return Response(
                {'error': 'Elemento no encontrado.'},
                status=status.HTTP_404_NOT_FOUND,
            )

        data = request.data
        if 'id' not in data or str(data.get('id')) != id:
            return Response(
                {'error': 'El campo id es obligatorio y debe coincidir con el identificador en la URL.'},
                status=status.HTTP_400_BAD_REQUEST,
            )

        if 'name' not in data or 'email' not in data:
            return Response(
                {'error': 'Faltan campos requeridos: name y email.'},
                status=status.HTTP_400_BAD_REQUEST,
            )

        item.clear()
        item.update({
            'id': id,
            'name': data['name'],
            'email': data['email'],
            'is_active': data.get('is_active', True),
        })

        return Response(
            {'message': 'Elemento reemplazado correctamente.', 'data': item},
            status=status.HTTP_200_OK,
        )

    def patch(self, request, id):
        item = self.get_item(id)
        if item is None:
            return Response(
                {'error': 'Elemento no encontrado.'},
                status=status.HTTP_404_NOT_FOUND,
            )

        data = request.data
        if 'id' in data and str(data.get('id')) != id:
            return Response(
                {'error': 'El campo id en el cuerpo debe coincidir con el identificador en la URL.'},
                status=status.HTTP_400_BAD_REQUEST,
            )

        item.update({
            key: value for key, value in data.items() if key != 'id'
        })

        return Response(
            {'message': 'Elemento actualizado correctamente.', 'data': item},
            status=status.HTTP_200_OK,
        )

    def delete(self, request, id):
        item = self.get_item(id)
        if item is None:
            return Response(
                {'error': 'Elemento no encontrado.'},
                status=status.HTTP_404_NOT_FOUND,
            )

        item['is_active'] = False
        return Response(
            {'message': 'Elemento eliminado lógicamente.'},
            status=status.HTTP_200_OK,
        )

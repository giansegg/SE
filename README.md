# Pruebas Unitarias para el Sistema de Cálculo de Distancia entre Ciudades

Los casos incluyen verificaciones para tres servicios: `APIService`, `MockService` y `CSVService`.

## Casos de Prueba

| Test Case                                  | Precondition                          | Test Steps                                                                                                                      | Test Data                               | Expected Result                                                                     |
| ------------------------------------------ | ------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------- | ----------------------------------------------------------------------------------- |
| **CSVService - Ciudad no encontrada**      | La ciudad no existe en el CSV         | 1. Mockear `csv_service.get_coords` para devolver `None` <br> 2. Llamar endpoint con ciudad inexistente                         | Ciudad: NOEXISTE <br> País: FantasyLand | La respuesta debe ser 404 con el error `{'error': 'City not found'}`                |
| **CSVService - Misma ciudad**              | La misma ciudad se ingresa dos veces  | 1. Mockear `csv_service.get_coords` para devolver coordenadas específicas <br> 2. Llamar endpoint con la misma ciudad dos veces | Ciudad: New York <br> País: USA         | La distancia calculada debe ser `0`, ya que es la misma ciudad                      |
| **APIService - Ciudad válida**             | La ciudad y el país existen en el API | 1. Llamar a `APIService.get_coords` con una ciudad válida <br> 2. Verificar que devuelve coordenadas                            | Ciudad: Tokyo <br> País: Japan          | Se deben obtener coordenadas válidas (`lat` y `lng`) para la ciudad especificada    |
| **APIService - Ciudad inválida**           | La ciudad no existe en el API         | 1. Llamar a `APIService.get_coords` con una ciudad inexistente <br> 2. Verificar que devuelve `None`                            | Ciudad: INEXISTENTE <br> País: NOEXISTE | Debe devolver `None`, indicando que la ciudad no se encontró                        |
| **MockService - Coordenadas siempre cero** | No se requieren condiciones           | 1. Llamar a `MockService.get_coords` con cualquier entrada <br> 2. Verificar que devuelve coordenadas cero                      | Ciudad: Cualquier <br> País: Cualquier  | Siempre debe devolver `{ "lat": 0, "lng": 0 }`, sin importar los valores de entrada |

### Notas:

- **CSVService** está siendo probado con mocks para simular el comportamiento de un servicio basado en archivos CSV. Los casos incluyen tanto la verificación de una ciudad inexistente como la distancia para la misma ciudad.
- **APIService** realiza una consulta real de coordenadas en una API. Los casos de prueba cubren tanto consultas válidas como inválidas.
- **MockService** está diseñado para devolver coordenadas fijas `{ "lat": 0, "lng": 0 }`, independientemente de la ciudad o país de entrada, lo cual es verificado en su caso de prueba.

Estos casos de prueba están diseñados para cubrir tanto condiciones de éxito como casos extremos de entrada de datos en cada servicio específico.

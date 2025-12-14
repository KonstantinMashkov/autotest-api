from typing import TypedDict
from httpx import Response
from clients.api_client import APIClient


class RequestCreateExercisesViewDict(TypedDict):
    title: str
    courseId: str
    maxScore: int
    minScore: int
    orderIndex: int
    description: str
    estimatedTime: str
    

class RequestUpdateExercisesViewDict(TypedDict):        
    title: str | None
    maxScore: int | None
    minScore: int | None
    orderIndex: int | None
    description: str | None
    estimatedTime: str | None
    
    

class ExercisesClient(APIClient):
    def get_exercises_view_api(self, query: str) -> Response:
        return self.get(f'/api/v1/exercises', params=query)
    
    def post_create_exercises_view_api(self, request: RequestCreateExercisesViewDict) -> Response:
        return self.post(f'/api/v1/exercises', json=request)
    
    def get_exercises_view_exercises_id_api(self, exercise_id: str) -> Response:
        return self.get(f'/api/v1/exercises/{exercise_id}')
    
    def patch_update_exercises_view_api(self, exercise_id: str, request: RequestUpdateExercisesViewDict) -> Response:
        return self.patch(f'/api/v1/exercises/{exercise_id}', json=request)
    
    def delete_exercises_view_api(self, exercise_id: str) -> Response:
        return self.get(f'/api/v1/exercises/{exercise_id}')
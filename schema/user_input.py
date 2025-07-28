from pydantic import BaseModel, Field, computed_field, field_validator
from typing import Literal, Annotated
from config.city_tier import tier_1_cities, tier_2_cities
# pydantic model to validate incoming data

class UserInput(BaseModel):
    age: Annotated[int, Field(..., gt = 0, lt =100, description= "ENter your age")]
    weight: Annotated[float, Field(..., gt = 0, description= "ENter your weight in kgs")]
    height: Annotated[float, Field(..., gt = 0, description= "ENter your height")]
    income_lpa: Annotated[int, Field(..., gt = 0, lt =100, description= "ENter your income")]
    smoker: Annotated[bool, Field(default= False, description="Are you a smoker?")]
    city: Annotated[str, Field(..., description= "Enter your city name")]
    occupation: Annotated[Literal['retired', 'freelancer', 'student', 'government_job',
       'business_owner', 'unemployed', 'private_job'], Field(..., description='Occupation of the user')]
    
    @field_validator('city')
    @classmethod
    def normalize_city(cls, v: str) -> str:
        v = v.strip().title()
        return v
    
    @computed_field
    @property
    def BMI(self) -> float:
        BMI= round(self.weight/(self.height**2), 2)
        return BMI
    
    @computed_field
    @property
    def lifestyle_risk(self) -> str:
        if self.smoker and self.BMI > 30:
            return "High"
        elif self.smoker or self.BMI > 27:
            return 'Median'
        else: 
            return "Low"
        
    
    @computed_field
    @property
    def age_group(self) -> str:
        if self.age < 25:
            return "Young"
        elif self.age < 45:
            return 'Adult'
        elif self.age < 65:
            return 'Middle age'
        return 'Senior'
    
    @computed_field
    @property
    def city_tier(self) -> int:
        if self.city in tier_1_cities:
            return 1
        elif self.city in tier_2_cities:
            return 2
        else:
            return 3
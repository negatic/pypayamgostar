import requests
import json
from decimal import Decimal


class Appointment:
    ''' Class for Creating and Deleting Appointments '''
    def create(self,
            CrmId:str,
            ParentCrmObjectId:str,
            CrmObjectTypeName:str,
            CrmObjectTypeCode:str,
            CreateDate:str,
            ModifyDate:str,
            RefId:str,
            Stage:str,
            IdentityId:str,
            Description:str,
            Subject:str,
            Location:str,
            StartDatePersian:str,
            StartDate:str,
            EndDate:str,
            EndDatePersian:str,
            CalendarId:str,
            CalendarName:str,
            Latitude:str,
            Longitude:Decimal,
            AssignedToId:str,
            AppointmentAttendantsInfo:list,
            Tags:list,
            ExtendedProperties:list,
            CrmObjectTypeId:str,
            CrmObjectTypeIndex:int,
            RoomType:str,
            ProcessStateIndex:int,
            StageId:str,
            AppointmentStatus:str
            ):

        data = locals()
        del data['self']
        data['userName'] = self.username; data['password'] = self.password
        data = json.dumps(data)
        requests.post(url=self.url,data=data)

    def delete(self,appointmentId:str):
        data = {'appointmentId':appointmentId,
                'userName':self.username,
                'password':self.password
                }
        data = json.dumps(data)
        requests.post(url=self.url,data=data)


class Person:
    ''' Class for Creating and Deleting a Person '''
    def create(self,
            CrmObjectTypeCode:str,
            FirstName:str,
            LastName:str,
            IdentityType:str,
            Categories:dict,
            PhoneContacts:dict,
            Emails:dict,
            Subject:str,
            RefId:str,
            Website:str,
            NationalCode:str,
            Balance:Decimal,
            SourceType:str,
            BirthDate:str,
            Gender:str,
            CustomerNumber:str,
            CustomerDate:str,
            OtherUserName:str,
            SaleUsername:str,
            SupportUsername:str,
            ColorName:str,
            AddressContacts:dict,
            Degree:str,
            CreditType:str
            ):
    
        data = locals()
        del data['self']
        data['userName'] = self.username; data['password'] = self.password
        data = json.dumps(data)
        requests.post(url=self.url,data=data)
    
    
    def delete(self,PersonId:str):

        data = {'appointmentId':PersonId,
        'userName':self.username,
        'password':self.password
        }
        data = json.dumps(data)
        requests.post(url=self.url,data=data)

class Pypg(Appointment):
    def __init__(self,url:str,username:str,password:str) -> None:
        self.url = url
        self.username = username
        self.password = password
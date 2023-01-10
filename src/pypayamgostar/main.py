import requests
from decimal import Decimal


class Appointment:
    def __init__(self) -> None:
        pass

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
        requests.post(url=self.url,data=data)

    def delete(self,appointmentId:str):
        data = {'appointmentId':appointmentId,
                'userName':self.username,
                'password':self.password
                }
        requests.post(url=self.url,data=data)

class Pypg(Appointment):
    def __init__(self,url:str,username:str,password:str) -> None:
        self.url = url
        self.username = username
        self.password = password


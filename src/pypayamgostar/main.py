import requests
import json
from decimal import Decimal

class Pypg():
    '''Main Class Responsible For Instantiating a Connection to The Webservice'''
    def __init__(self,url:str,username:str,password:str) -> None:
        self.url = url
        self.username = username
        self.password = password

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
        requests.post(url=f'{self.url}/Services/API/IAppointment.svc',data=data)

    def delete(self,appointmentId:str):
        data = {'appointmentId':appointmentId,
                'userName':self.username,
                'password':self.password}
        data = json.dumps(data)
        requests.delete(url=f'{self.url}/Services/API/IAppointment.svc',data=data)


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
        requests.post(url=f'{self.url}/services/api/IPerson.svc',data=data)
    
    
    def delete(self,person_id:str):
        data = {'appointmentId':person_id,
        'userName':self.username,
        'password':self.password}
        data = json.dumps(data)
        requests.delete(url=f'{self.url}/services/api/IPerson.svc',data=data)

class Inventory:

    def get_remaining_stock(self,product_code:str):
        data = {'product_code':product_code,
        'userName':self.username,
        'password':self.password
        }
        data = json.dumps(data)
        requests.post(url=f'{self.url}/services/api/IInventory.svc',data=data)

class Opportunity:
    '''Class for Creating and Deleting Opportunities'''
    def create(self,
        opportunityinfo:dict,
        CrmId:str,
        ParentCrmObjectId:str,
        CrmObjectTypeName:str,
        CrmObjectTypeCode:str,
        ExtendedProperties:dict,
        CreateDate:str,
        ModifyDate:str,
        Tags:list,
        RefId=str,
        Stage=str,
        IdentityId=str,
        Description=str,
        Subject=str,
        SaleStage=str,
        OpportunityType=str,
        OpportunitySourceType=str,
        WonCause=str,
        LostCause=str,
        ClosedDatePersian=str,
        ClosedDate=str,
        TotalValue=Decimal,
        Probability=Decimal,
        TotalDiscount=Decimal,
        FailDate=str,
        SuccessDate=str,
        ProcessStateIndex=int,
        StageId=str,
        Name=str,
        Value=str,
        UserKey=str
        ):

        data = locals()
        del data['self']
        data['userName'] = self.username; data['password'] = self.password
        data = json.dumps(data)
        requests.post(url=f'{self.url}/services/api/IOpportunity.svc',data=data)
    
    def delete(self,opportunity_id:str):
        data = {'appointmentId':opportunity_id,
        'userName':self.username,
        'password':self.password}
        data = json.dumps(data)
        requests.delete(url=f'{self.url}/Services/API/IAppointment.svc',data=data)

class Ticket:
    def create(self,
            ticketInfo:dict,
            CrmId:str,
            ParentCrmObjectId:str,
            CrmObjectTypeCode:str,
            ExtendedProperties:list,
            CreateDate:str,
            ModifyDate:str,
            Tags:list,
            RefId:str,
            Stage:str,
            IdentityId:str,
            Description:str,
            Subject:str,
            Status:str,
            EmailAddress:str,
            AssignedTo:str,
            ResponseStatus:str,
            Impact:str,
            Number:int,
            Severity:str,
            CrmObjectTypeId:str,
            CrmObjectTypeIndex:int,
            StageId:str,
            Name:str,
            Value:str,
            UserKey:str):

        data = locals()
        del data['self']
        data['userName'] = self.username; data['password'] = self.password
        data = json.dumps(data)
        requests.post(url=f'{self.url}/services/api/iticket.svc',data=data)
    
    def delete(self,ticketId:str):
        data = {'appointmentId':ticketId,
        'userName':self.username,
        'password':self.password}
        data = json.dumps(data)
        requests.delete(url=f'{self.url}/Services/API/iticket.svc',data=data)

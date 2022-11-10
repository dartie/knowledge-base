# Salesforce API

## Query with dates
* https://developer.salesforce.com/docs/atlas.en-us.soql_sosl.meta/soql_sosl/sforce_api_calls_soql_select_dateformats.htm
* https://developer.salesforce.com/forums/?id=906F00000008m41IAA

```SQL
SELECT Id, Name, Email, Phone, AccountId
FROM   Contact
WHERE  (Name = 'Some Name 1' AND Email = 'Some Email 1' AND Phone = 'Some Phone 1' AND AccountId = 'Some AccountId 1') OR
     (Name = 'Some Name 2' AND Email = 'Some Email 2' AND Phone = 'Some Phone 2' AND AccountId = 'Some AccountId 2')
```


## Results to Pandas dataframe

```python
from simple_salesforce import Salesforce
sf = Salesforce(username='<enter username>', password='<enter password>', 
   security_token = '<enter your access token from your profile>')

a_query= pd.DataFrame(sf.query(
   "SELECT Name, CreatedDate FROM User")['records'])
```



# 📦 Inventory-API 📦

## How to Access

Click the following link, the framework fastAPI provides an swagger interface to test the api endpoints.

Link: https://inventory-api-shopify.herokuapp.com/docs#/


## How to Interact

Endpoints are grouped by a particular set of functionality. For instance all product related endpoints are underneath the "Products" tag.

![image](https://user-images.githubusercontent.com/37748500/148620183-a1b03e86-7525-4739-b05d-f118e0f3aaf1.png)

Each type of request can be expanded. In order to execute a particular endpoint, swagger provides a "try it out button" when expanded.

![image](https://user-images.githubusercontent.com/37748500/148620268-ff59c3f7-a036-4f74-bfdf-c9c051e12a20.png)

Upon clicking try it out, any required path parameters or request bodies will be editable. 

![image](https://user-images.githubusercontent.com/37748500/148620366-d072e467-1761-4ba9-b8f3-fdfaa839279a.png)

If you are curious which fields in a request body are optional you can select the Schema tab on the request body example.
A red star indicates that it must be included in the request. In order to see this tab, you be out of "try it out", you can click the 
cancel button in the top right if you have clicked "try it out".

![image](https://user-images.githubusercontent.com/37748500/148620519-927a0822-b531-4835-85c7-b2f5be0f03b5.png)

If you scroll to the bottom of an endpoint example, you can view the response schema of the request. Where a product id or warehouse id is required,
you can use the get endpoint to retrieve a list of all warehouses and products which will include their ids as the _id field. 

# Assignment-4
INTEGRATED EXTERNAL SERVICE.
**Simple calculator API**
----
  Returns json data of simple calculator output.

* **URL**

  /api

* **Method:**

  `GET`
  
* **Data Params**

   **Required:**
 
   `op1=[integer], op2=[integer], op=[string]`


* **Success Response:**

  * **op1 = 4** <br />
    **op2 = 2** <br />
    **op = +** <br />
    **Code:** 200 <br />
    **Content:** `{"answer": 6}`
 
* **Error Response1:**

  * **op1 = "4"** <br />
    **op2 = "2"** <br />
    **op = "$"** <br />
    **Code:** 500 INTERNAL SERVER ERROR <br />
    **Content:** `{"message": "Internal Server Error"}`
    
    **Error Response2:**

  * **op1 = "4"** <br />
    **op2 = "B"** <br />
    **op = "+"** <br />
    **Code:** 404 NOT FOUND <br />
    **Content:** `The requested URL was not found on the server. If you entered the URL manually please check your spelling and try again.`


* **Description:**

     The html file is opened and the operands and operators are inputed into the respective text fields. When the submit button is pressed, the result of the corresponding operation is returned. 
     
**Currency Convertor API**
----
 Returns json data of USD to EURO currency converter output.

* **URL**

  /currencyConverter

* **Method:**

  `GET`
  
* **Data Params**

   **Required:**
 
   `amount=[integer]`


* **Success Response:**

  * **amount = 6** <br />
    **Code:** 200 <br />
    **Content:** `{"converted": "5.629194"}`
 
    **Error Response:**

  * ***amount = ")"** <br />
    **Code:** 404 NOT FOUND <br />
    **Content:** `The requested URL was not found on the server. If you entered the URL manually please check your spelling and try again.`


* **Description:**

     The html file is opened and the amount of USD to be converted is inputed into the respective text field. When the "convert" button is pressed, the corresponding EURO value is returned. 
     
  ```


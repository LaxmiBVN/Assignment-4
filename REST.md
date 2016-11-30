# Assignment-2 & Assignment-3
Convert Your Website Into a Basic ReSTful WebService.
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

     To perform arithmetic operation: url: http://54.244.41.255:5000/4/2/+ parameter : Enter the oparands value and the operator to perform the calculation  output : {"answer": "6"}

     
  ```


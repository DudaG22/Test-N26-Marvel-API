# Test-N26-Marvel-API
The test consists of outputting a python dataframe and .csv file, making request to the Marvel's Characters API

The Marvel's API needs a hash MD5 encryption to be accessed.
Were provided two keys, private key and public key.

Following, the API Authentication guidelines:

"Authentication for Server-Side Applications
Server-side applications must pass two parameters in addition to the apikey parameter:

ts - a timestamp (or other long string which can change on a request-by-request basis)
hash - a md5 digest of the ts parameter, your private key and your public key (e.g. md5(ts+privateKey+publicKey)

For example, a user with a public key of "1234" and a private key of "abcd" could construct a valid call as follows: http://gateway.marvel.com/v1/public/comics?ts=1&apikey=1234&hash=ffd275c5130566a2916217b101f26150 (the hash value is the md5 digest of 1abcd1234)"

After gaining access, the next step is to make the request:
The API have a pagination limit = 100, so it's neded to make loop using the offset parameter to have the complete API.
Offset parameter receives a incremnt of 100 each loop, and the data is stored in a DataFrame

The DataFrame is converted in a group of lists;
Each list will be a column in the future, so the data is filtered before being added to the list.

The final DataFrame is created using the filtred lists
The last step is print the final DataFrame.

(the 'DataFrame.to_csv()' comand can be used to create de .csv file)

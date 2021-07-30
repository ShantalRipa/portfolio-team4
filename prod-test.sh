#!/bin/bash
# Script to test backend routes of the portfolio
domain='https://week2-mlh-domain-demo.duckdns.org'
endpoints=("/" "/register" "/login")
error=0
for endpoint in "${endpoints[@]}"
do
   url="${domain}${endpoint}"
   status=$(curl -s -o /dev/null -w "%{http_code}" "${url}")
   printf "#### Testing route: ${endpoint} -> Status: ${status} ####\n"
   if [[ $status -ne 200 ]]
   then
       error=1
   fi  
done
exit $error

#! /bin/sh
#Test endpoints of domain

function test {
	domain="https://week2-mlh-domain-demo.duckdns.org"
	endpoints=("register" "login")

	#Generate random user and password
	username=$(date | md5sum)
	password=$(date | md5sum)
	
	for endpoint in "${endpoints[@]}"
	do
		url="${domain}/${endpoint}"
		curl -X POST -d "username=${username}&password=${password}" "${url}"
	done
}

test

#!/bin/bash
RANDNUM="`shuf -i 20000-50000 -n 1`"
cp vars.yml vars-myvars.yml
sed -i "s/RANDOM/$RANDNUM/g" vars-myvars.yml
vmname="`grep vm_name vars-myvars.yml | awk '{print $2}'`"
newvmname="`echo $vmname | tr '[:upper:]' '[:lower:]' | sed 's/[^a-z0-9]//g' | cut -c 1-15`"
sed -i "s/$vmname/$newvmname/g" vars-myvars.yml
echo "Your random number vars file is vars-myvars.yml"

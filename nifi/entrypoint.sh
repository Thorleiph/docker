#!/bin/bash

export JAVA_HOME=$(readlink -f /etc/alternatives/java | sed 's/\/bin\/java//')

case "$1" in
	bash)
		/bin/bash
	;;

	*)
		/opt/apache/nifi/nifi-2.6.0/bin/nifi.sh run
	;;
esac

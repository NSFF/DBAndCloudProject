#!/usr/bin/env bash
docker tag local-image:tagname new-repo:tagname
docker push new-repo:tagname
#!/bin/bash

EXPECTED="3 Record(s) inserted"
RESULT=$(bash import.sh capterra feed-products/capterra.yaml)
if echo "$RESULT" | grep -q "$EXPECTED"; then
  echo "Test passed";
else
  echo "Test failed";
fi

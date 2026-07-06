*** Variables ***
${PLATAFORMA}        android
${APPIUM_SERVER}   http://127.0.0.1:4723

*** Settings ***
Resource    ./capabilities_${PLATAFORMA}.robot

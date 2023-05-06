while sleep 0.1;
  do
     curl -X GET https://127.0.0.1.tm.sslip.io/combined_data --cacert ./telemedicinebff/app/ca.crt
    echo "";
  done ;
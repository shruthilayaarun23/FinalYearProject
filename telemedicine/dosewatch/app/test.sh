while sleep 0.1; 
  do 
    curl -X POST -F 'p_id=1' https://127.0.0.1.dw.sslip.io/dose-watch/read --cacert ./dosewatch/istio/ca.crt
    echo ""; 
  done ;
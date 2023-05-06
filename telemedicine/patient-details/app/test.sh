while sleep 0.1; 
  do 
    curl -X POST -F 'p_id=1' https://127.0.0.1.pd.sslip.io/patient-details/read --cacert ./patient-details/istio/ca.crt
    echo ""; 
  done ;
while sleep 0.1; 
  do 
    curl -X GET  https://127.0.0.1.pi.sslip.io/patient_imaging/getAllPatients --cacert ./patient-imaging/istio/ca.crt
    echo ""; 
  done ;
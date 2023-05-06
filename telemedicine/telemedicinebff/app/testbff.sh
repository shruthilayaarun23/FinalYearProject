for p_id in 1 2 3; do
  for study_id in 708a2528-b512164c-0f547574-dfbad394-88a66bdc b70f4372-7fc370d7-c2767fff-d95a07a1-99a7fa16 6a433dd4-6deccce3-18891f14-44676dd3-8e672ed0; do
    curl -X GET "https://127.0.0.1.tm.sslip.io/combined_data/$p_id/$study_id" --cacert ./telemedicineapp/app/ca.crt
    echo ""
  done
done

  
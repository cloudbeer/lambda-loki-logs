## use kinesis data stream


terraform apply -var "lambda_promtail_image=320236118172.dkr.ecr.us-west-2.amazonaws.com/lambda-promtail:main-bc78d13-amd64" \
  -var "write_address=http://34.223.23.146:3100/loki/api/v1/push" \
  -var 'kinesis_stream_name=["kds-lambda-hello"]' \
  -var 'extra_labels=app,kds-logs' -var "omit_extra_labels_prefix=true" \
  -var "tenant_id=1" 




## use cloudwatch log group
# terraform apply -var "lambda_promtail_image=<repo:tag>" 
# -var "write_address=https://logs-prod-us-central1.grafana.net/loki/api/v1/push" 
# -var "password=<password>" -var "username=<user>" 
# -var 'log_group_names=["/aws/lambda/log-group-1", "/aws/lambda/log-group-2"]' 
# -var 'bucket_names=["bucket-a", "bucket-b"]' -var 'batch_size=131072'



# https://grafana.com/docs/loki/latest/send-data/lambda-promtail/
# -var "password=<basic-auth-pw>" \
# -var "username=<basic-auth-username>" \
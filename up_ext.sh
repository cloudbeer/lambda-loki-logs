echo "准备 extension"
chmod +x extensions/loki-kds-extension
zip -qr /tmp/loki-kds-ext-layer.zip ./extensions

echo "部署 extension Layer "
aws lambda publish-layer-version \
    --layer-name loki-kds-ext-layer \
    --region us-west-2 \
    --zip-file fileb:///tmp/loki-kds-ext-layer.zip


echo "准备 dependencies"
echo "copy files 这一步是为了不要污染源代码目录，因为依赖包要和源代码在同一级目录"
cp -f loki-kds-extension/logs_api_http_extension.py loki-kds-extension/loki-kds-extension
cp -rf loki-kds-extension/logs_api_http_extension loki-kds-extension/loki-kds-extension

chmod +x loki-kds-extension/loki-kds-extension/logs_api_http_extension.py

echo "打包 依赖包 zip -q -r"
rm /tmp/loki-kds-layer.zip 
cd ./loki-kds-extension
# 这里要保留目录 loki-kds-extension
zip -qr /tmp/loki-kds-layer.zip ./loki-kds-extension

echo "部署 Layer loki-kds-extension "
aws lambda publish-layer-version \
    --layer-name loki-kds-layer \
    --region us-west-2 \
    --zip-file fileb:///tmp/loki-kds-layer.zip


echo "更新配置 aws lambda update-function-configuration"

aws lambda update-function-configuration \
    --function-name lambda-loki-logs-HelloWorldFunction-y3EcDI21TMKY \
    --region us-west-2 \
    --layers  arn:aws:lambda:us-west-2:320236118172:layer:loki-kds-ext-layer:5 \
              arn:aws:lambda:us-west-2:320236118172:layer:loki-kds-layer:30
            



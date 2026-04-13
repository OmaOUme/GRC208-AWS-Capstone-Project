content = open('cloudformation-database-stack.yaml').read()
content = content.replace(
    '          - ServerSideEncryptionByDefault:\n            SSEAlgorithm: \'aws:kms\'\n            KMSMasterKeyID: !GetAtt S3EncryptionKey.Arn',
    '          - ServerSideEncryptionByDefault:\n              SSEAlgorithm: \'aws:kms\'\n              KMSMasterKeyID: !GetAtt S3EncryptionKey.Arn'
)
open('cloudformation-database-stack.yaml', 'w').write(content)
print('Done')

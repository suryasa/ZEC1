import marshal,zlib,base64
exec(zlib.decompress(base64.b64decode("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")))
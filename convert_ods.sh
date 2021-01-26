#!/bin/bash

#---- Parameters
SRC_FILE="report"   #-- orginal .xls file
TARGET_FILE="listado_orig"  #-- Target ods filename

# ----- Convert the report.xls file to ods format  
soffice --headless --convert-to ods $SRC_FILE.xls

# ----- Generate the target file
mv $SRC_FILE.ods $TARGET_FILE.ods

echo "FICHERO GENERADO: $TARGET_FILE.ods"

library(data.table)
library(dplyr)
library(arrow)

# replace path to prep_data:
setwd('/prep_data')

# BPATG
dt_bpatg <-fread("CE-BPatG_2024-07-09_DE_CSV_Datensatz.csv")
write_feather(dt_bpatg, "dt_bpatg.feather")

# BGH
dt.bgh <-fread("CE-BGH_2024-09-25_DE_CSV_Datensatz.csv")

dt_zs10a <- dt.bgh %>% filter(spruchkoerper_db == "Zivilsenat-10a")
write_feather(dt_zs10a, "dt_zs10a.feather")


dt_zs10 <- dt.bgh %>% filter(spruchkoerper_db == "Zivilsenat-10")
write_feather(dt_zs10, "dt_zs10.feather")





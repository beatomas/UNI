#!/bin/bash

grep -v NA pseudo_facebook.csv >> processed1_pseudo_facebook.csv
awk -F',' '{if($2>=16 && $2<=75) print $0}' processed1_pseudo_facebook.csv >> processed2_pseudo_facebook.csv
awk -F',' '{if($8>=25) print $0}' processed2_pseudo_facebook.csv >> processed3_pseudo_facebook.csv
awk -F',' '{if($11>=100) print $0}' processed3_pseudo_facebook.csv >> processed4_pseudo_facebook.csv
awk -F',' '{if($7<365 && $11>3000 && $8<100)print $0",Fake,"($10/$11)*100
	else if($8>500 && $11>3000)print $0",Influencer,"($10/$11)*100
	else if($8<50 || $11<200 && $7>365)print $0",Non-target,"($10/$11)*100
	else print $0",Normal,"($10/$11)*100}' processed4_pseudo_facebook.csv >> processed5_pseudo_facebook.csv
echo -e "user_id\tage\tdob_day\tdob_year\tdob_month\tgender\ttenure\tfriend_count\tfriendships_initiated\tlikes\tlikes_received\tmobile_likes\tmobile_likes_received\twww_likes\twww_likes_received\tInterest\tReciprocity" | cat - processed5_pseudo_facebook.csv > processed_pseudo_facebook.csv
rm -r processed1_pseudo_facebook.csv
rm -r processed2_pseudo_facebook.csv
rm -r processed3_pseudo_facebook.csv
rm -r processed4_pseudo_facebook.csv
rm -r processed5_pseudo_facebook.csv
rm -r pseudo_facebook.csv


echo 'Introdueix un identificador per a un usuari:'
read usuari
if (grep -w "^$usuari" processed_pseudo_facebook.csv); then
	x=True
else	
	echo "No hi ha ningún usuari que coincideixi."
fi

chmod +x dataset.sh


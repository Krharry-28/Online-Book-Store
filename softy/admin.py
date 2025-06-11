from django.contrib import admin
from softy.models import CBGN, DM, HF, LF, Act_Adv, All_Book, Classics,  Contact, Fantasy, Horror, Sci_fi
# Register your models here.

admin.site.register(Contact),
#admin.site.register(Signup),
admin.site.register(Act_Adv),
admin.site.register(Classics),
admin.site.register(CBGN),
admin.site.register(DM),
admin.site.register(Fantasy),
admin.site.register(HF),
admin.site.register(Horror),
admin.site.register(LF),
admin.site.register(Sci_fi),
admin.site.register(All_Book),



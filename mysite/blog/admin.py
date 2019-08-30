from django.contrib import admin
from blog.models import Post, Comment, appointment, ProdID, Book, ProgramaConv, PruebaMod, PruebaTabla, OrdenProg, DetalleProg, ProdReal, Maquinas, Turnos, Minuta, OrderInfo, Padron, DiaConv2, OrdenProgCorr, DetalleProgCorr, Meses, Semanas, FotoInventario, ProyMkt, ProyMktMes, ProyMktPadron, ProdRealCorr, InfoWIP, Camion, OrdenCorrplan, FotoCorrplan, Cartones, CalleBPT, BobInvCic, MovPallets


# Register your models here.
admin.site.register(Post)
admin.site.register(Comment)#Cuando se agregan estos hay que aplicar el migrate

admin.site.register(appointment)#Cuando se agregan estos hay que aplicar el migrate
admin.site.register(ProdID)#Cuando se agregan estos hay que aplicar el migrate
admin.site.register(Book)#Cuando se agregan estos hay que aplicar el migrate
admin.site.register(ProgramaConv)#Cuando se agregan estos hay que aplicar el migrate
admin.site.register(PruebaMod)#Cuando se agregan estos hay que aplicar el migrate
admin.site.register(PruebaTabla)#Cuando se agregan estos hay que aplicar el migrate
admin.site.register(OrdenProg)#Cuando se agregan estos hay que aplicar el migrate
admin.site.register(DetalleProg)#Cuando se agregan estos hay que aplicar el migrate
admin.site.register(ProdReal)#Cuando se agregan estos hay que aplicar el migrate
admin.site.register(Maquinas)#Cuando se agregan estos hay que aplicar el migrate
admin.site.register(Turnos)#Cuando se agregan estos hay que aplicar el migrate
admin.site.register(Minuta)#Cuando se agregan estos hay que aplicar el migrate
admin.site.register(OrderInfo)#Cuando se agregan estos hay que aplicar el migrate
admin.site.register(Padron)#Cuando se agregan estos hay que aplicar el migrate
admin.site.register(DiaConv2)#Cuando se agregan estos hay que aplicar el migrate
admin.site.register(OrdenProgCorr)#Cuando se agregan estos hay que aplicar el migrate
admin.site.register(DetalleProgCorr)#Cuando se agregan estos hay que aplicar el migrate
admin.site.register(Meses)#Cuando se agregan estos hay que aplicar el migrate
admin.site.register(Semanas)#Cuando se agregan estos hay que aplicar el migrate
admin.site.register(FotoInventario)#Cuando se agregan estos hay que aplicar el migrate
admin.site.register(ProyMkt)#Cuando se agregan estos hay que aplicar el migrate
admin.site.register(ProyMktMes)#Cuando se agregan estos hay que aplicar el migrate
admin.site.register(ProyMktPadron)#Cuando se agregan estos hay que aplicar el migrate
admin.site.register(ProdRealCorr)#Cuando se agregan estos hay que aplicar el migrate
admin.site.register(InfoWIP)#Cuando se agregan estos hay que aplicar el migrate
admin.site.register(Camion)#Cuando se agregan estos hay que aplicar el migrate
admin.site.register(OrdenCorrplan)#Cuando se agregan estos hay que aplicar el migrate
admin.site.register(FotoCorrplan)
admin.site.register(Cartones)
admin.site.register(CalleBPT)
admin.site.register(BobInvCic)
admin.site.register(MovPallets)

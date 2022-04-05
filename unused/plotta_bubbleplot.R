#require("verification")
#require("ggplot2")
source("tabella_dataset.R")
########################

bolle.macro<-function(dati,model,maxbolla,grafica){
    br<-c(-1,5,25,50,75,100,150,1000)  
    cl.o<-cut(dati$B13011.x,breaks=br)
    cl.p<-cut(dati$B13011.y,breaks=br)
    tabb<-table(cl.o,cl.p)
    classi<-c("]0-5]","]5-25]","]25-50]","]50-75]","]75-100]","]100-150]",">150")
    bolle<-expand.grid(classi,classi)
    bolle$value<-as.data.frame(tabb)$Freq
    bolle$X<-as.numeric(bolle$Var1)
    bolle$Y<-as.numeric(bolle$Var2)
    oss.lab<-"Obs (mm)"
    pre.lab<-"Fcst (mm)"
    
    if(grafica){
                                        #titolo<-"prova"
        radius<-sqrt(bolle$value/pi)
        inc<-0.45*max(radius)/sqrt(maxbolla/pi)
        col<-colormod(model)
        radius<-sqrt(bolle$value/pi)
        symbols(bolle$X,bolle$Y,circles=radius,bg="gray",fg="gray",inches=inc,lwd=2,xlab=oss.lab,ylab=pre.lab,cex.axis=1.2,cex.lab=1.5,xaxt="n",yaxt="n",panel.first={abline(v=seq(0.5,8),h=seq(0.5,8),col="gray",lty=2);rect(xleft=seq(0.5,6.5),ybottom=seq(0.5,6.5),xright=seq(1.5,7.5),ytop=seq(1.5,7.5),col="azure",lty=2,border="gray")})
        axis(1,classi,at=seq(1,7),cex.axis=1.4)
        axis(2,classi,at=seq(1,7),cex.axis=1.4)
        testo<-ifelse(bolle$value>0,bolle$value,"")
        text(bolle$X,bolle$Y,labels=testo,cex=1.7,col=col)
        title(nomemod(model),col=col,cex.main=2.0)
    }
    return(bolle)
}

######################
#args<-commandArgs(T)
dirini<-getwd()
                                        #in args ci devono stare la dirdati_stagione, scad(es.48), max 3 modelli da confrontare (es.2I,5M,IFS)
args<-c("/autofs/scratch-mod/mstesini/NEW_VER_ITA/MAM2020","48","P_cosmo_2I_00_20200301_20200531_24.RData","P_cosmo_5M_ita_00_20200301_20200531_24.RData","P_ifs_ita010_00_20200301_20200531_24.RData")
if(length(args)<3) stop("argomenti da fornire: dirdati,scad,filedati") 
dirdati<-paste0(args[1],"/rdata")
                                        #setwd(dirdati)
nmod<-length(args)-2
scad<-args[2]
dirstag<-args[1]
dirbubble<-paste0(dirstag,"/","bubbleplot/")
dir.create(dirbubble,recursive=TRUE)
st<-unlist(strsplit(dirstag,"/"))
stag.titolo<-st[length(st)]
modelli<-c()
namemod<-c()
run<-c()
for (n in 1:nmod){
    modelli<-c(modelli,args[2+n])
    tmp<-unlist(strsplit(modelli[n],"_"))
    namemod<-c(namemod,paste(tmp[2:(length(tmp)-4)],collapse="_"))
    run<-c(run,sprintf("%02d",as.numeric(tmp[length(tmp)-3])))
    
}

                                        #carico dentro a una lista

dati.all<-vector("list",nmod)
for(n in 1:nmod){
    carico<-load(paste(dirdati,modelli[n],sep="/"))
    quale<-grep(scad,carico)
    dati.all[[n]]<-get(carico[quale])
    names(dati.all)[n]<-namemod[n]
}
                                        #per indicatore
for (ind in c("max","mean")){    
    dati<-vector("list",nmod)
    names(dati)<-namemod
    area.uni<-vector("list",nmod)
    for(i in 1:nmod){
        dtmp<-dati.all[[i]]
        dati[[i]]<-dtmp[,c("Date","B01192",paste0("B13011.",ind,".fcs"),paste0("B13011.",ind,".oss"))]
        names(dati[[i]])<-c("Date","id.a","B13011.y","B13011.x")
        area.uni[[i]]<-unique(dtmp$B01192)
    }
    
    aree<-Reduce(intersect,area.uni)
    for (a in 1:length(aree)){
                                        #calcolo il raggio massimo delle bolle
        maxb<-vector("list",nmod)   
        for (k in 1:nmod){
            btmp<-bolle.macro(dati[[k]][dati[[k]]$id.a==aree[a],],namemod[k],1,F)
            maxb[[k]]<-btmp$value
        }
        
        
        maxbolla<-Reduce(max,maxb)
        
                                        #plotto
        nomegrafico <-paste(dirbubble,ind,"_",stag.titolo,"_macro_",aree[a],"_",scad,".png",sep="")
        png(nomegrafico,width=1500,height=500)
        par(mfcol=c(1,3))
        for (k in 1:nmod){
            btmp<-bolle.macro(dati[[k]][dati[[k]]$id.a==aree[a],],namemod[k],maxbolla,T)
            
        }
        dev.off()
    }
}


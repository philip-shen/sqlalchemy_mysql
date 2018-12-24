#2018/11/25 Add class DellTest():
#2018/12/23 initial
####################################################################

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

class TWTSEOTCDaily(db.Model):
    __tablename__ = 'TSEOTCDaily'
    Id = db.Column(db.Integer, primary_key=True)
    trade_date = db.Column(db.String(64))
    trade_volumn = db.Column(db.String(128))
    trade_amount = db.Column(db.String(128))
    open_price = db.Column(db.String(64))
    high_price = db.Column(db.String(64))
    low_price = db.Column(db.String(64))
    close_price = db.Column(db.String(64))
    change = db.Column(db.String(64))
    tran_saction = db.Column(db.String(64))
    stkidx = db.Column(db.String(64))
    cmp_name = db.Column(db.String(64))

    def __init__(self
                 , trade_date
                 , trade_volumn
                 , trade_amount
                 , open_price
                 , high_price 
                 , low_price 
                 , close_price
                 , change 
                 , tran_saction 
                 , stkidx
                 , cmp_name
                 ):
        """Constructor"""
        if id:
            self.id = id   # Otherwise, default to auto-increment         
        self.trade_date = trade_date
        self.trade_volumn = trade_volumn
        self.trade_amount = trade_amount
        self.open_price = open_price
        self.high_price = high_price
        self.low_price = low_price
        self.close_price = close_price
        self.change = change
        self.tran_saction = tran_saction
        self.cmp_name = cmp_name

    def __repr__(self):
        """Show this object (database record)"""
        return "TSEOTCDaily(%d, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)" % (
            self.id, self.trade_date
            ,self.trade_volumn
            ,self.trade_amount
            ,self.open_price
            ,self.high_price
            ,self.low_price
            ,self.close_price
            ,self.change
            ,self.tran_saction
            ,self.cmp_name)

class GoogleDrive_callputjpg(db.Model):
    __tablename__ = 'CallPutJPG'
    Id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(25))
    title1 = db.Column(db.String(86))
    modifiedDate = db.Column(db.String(26))
    
    def __init__(self
                 , title
                 , title1
                 , modifiedDate
    #             , Remark
                 ):
        self.title = title
        self.title1 = title1
        self.modifiedDate = modifiedDate

class BulkInsertTest():
    def __init__(self,db,dbmodel_class):
        self.db = db
        self.dbmodel_class = dbmodel_class

    """Batched INSERT statements via the ORM in "bulk", discarding PKs."""
    def test_bulk_save(self,list_folderfiles):
        
        self.db.session.bulk_save_objects([
                #GoogleDrive_callputjpg(
                self.dbmodel_class(    
                title=dic_files['title'],
                title1=dic_files['title1'],
                modifiedDate=dic_files['modifiedDate']
                )
                for dic_files in list_folderfiles
        ])        
        

    """Batched INSERT statements via the ORM "bulk", using dictionaries."""
    def test_bulk_insert_mappings(self,list_folderfiles):

        self.db.session.bulk_insert_mappings(self.dbmodel_class, [#GoogleDrive_callputjpg, [
                    dic_files
                    for dic_files in list_folderfiles 
        ])        

'''***7.3  Using SQLAlchemy ORM (Object-Relational Mapper)***
http://www.ntu.edu.sg/home/ehchua/programming/webprogramming/Python3_Flask.html#zz-7.
****Flask-SQLAlchemy how to delete all rows in a single table***
https://stackoverflow.com/questions/16573802/flask-sqlalchemy-how-to-delete-all-rows-in-a-single-table'''
class DellTest():
    def __init__(self,db,dbmodel_class):
        self.db = db
        self.dbmodel_class = dbmodel_class
    
    def del_all(self):
        try:
            num_rows_deleted = self.db.session.query(self.dbmodel_class).delete()
            #self.db.session.commit()            
        except:
            self.db.session.rollback()

        return num_rows_deleted    

    def del_filterby_title(self,str_title):
        try:
            '''#for specific value
                db.session.query(Model).filter(Model.id==123).delete()'''
            instances_to_delete = self.db.session.query(self.dbmodel_class).filter_by(title=str_title).all()
            for instance in instances_to_delete:
                self.db.session.delete(instance)

            #self.db.session.commit()
        except:
            db.session.rollback()    


#2018/11/22 Fast SQLAlchemy counting (avoid query.count() subquery) 
#           https://gist.github.com/hest/8798884
def get_count(q):
    count_q = q.statement.with_only_columns([func.count()]).order_by(None)
    count = q.session.execute(count_q).scalar()
    return count

#if __name__ == '__main__':
#    manager.run()
from app.models import db, Post, Comment, Franchise
import time

def seed_posts():
    post_list= [
        Post(franchise_id="0001", create_date=str(time.time()), modify_date=str(time.time()), title="Testing 1, 2, 3", body="this is just a test, be ye not afraid of this, or the subsequent posts"),
        Post(franchise_id="0002", create_date=str(time.time()), modify_date=str(time.time()), title="Okay, time to copy some text", body="Session.add() is used to place instances in the session. For transient (i.e. brand new) instances, this will have the effect of an INSERT taking place for those instances upon the next flush. For instances which are persistent (i.e. were loaded by this session), they are already present and do not need to be added. Instances which are detached (i.e. have been removed from a session) may be re-associated with a session using this method:" ),
        Post(franchise_id="0003", create_date=str(time.time()), modify_date=str(time.time()), title="Deleting", body="Session.delete() marks an object for deletion, which will result in a DELETE statement emitted for each primary key affected. Before the pending deletes are flushed, objects marked by “delete” are present in the Session.deleted collection. After the DELETE, they are expunged from the Session, which becomes permanent after the transaction is committed."),
        Post(franchise_id="0004", create_date=str(time.time()), modify_date=str(time.time()), title="Flushing", body="When the Session is used with its default configuration, the flush step is nearly always done transparently. Specifically, the flush occurs before any individual SQL statement is issued as a result of a Query or a 2.0-style Session.execute() call, as well as within the Session.commit() call before the transaction is committed. It also occurs before a SAVEPOINT is issued when Session.begin_nested() is used."),
    ]
    comment_list= [
        Comment(franchise_id="0005", create_date=str(time.time()), modify_date=str(time.time()), post_id=1, body="Oh wow, that looks like an awesome test."),
        Comment(franchise_id="0006", create_date=str(time.time()), modify_date=str(time.time()), post_id=1, body="I feel so much calmer now."),
        Comment(franchise_id="0007", create_date=str(time.time()), modify_date=str(time.time()), post_id=1, body="Me Too!"),
        Comment(franchise_id="0001", create_date=str(time.time()), modify_date=str(time.time()), post_id=2, body="To add a list of items to the session at once, use Session.add_all():"),
        Comment(franchise_id="0002", create_date=str(time.time()), modify_date=str(time.time()), post_id=2, body="The Session.add() operation cascades along the save-update cascade. For more details see the section Cascades."),
        Comment(franchise_id="0004", create_date=str(time.time()), modify_date=str(time.time()), post_id=3, body="There are various important behaviors related to the Session.delete() operation, particularly in how relationships to other objects and collections are handled. There’s more information on how this works in the section Cascades, but in general the rules are:"),
        Comment(franchise_id="0002", create_date=str(time.time()), modify_date=str(time.time()), post_id=3, body="Rows that correspond to mapped objects that are related to a deleted object via the relationship() directive are not deleted by default. If those objects have a foreign key constraint back to the row being deleted, those columns are set to NULL. This will cause a constraint violation if the columns are non-nullable."),
        Comment(franchise_id="0003", create_date=str(time.time()), modify_date=str(time.time()), post_id=4, body="Regardless of the autoflush setting, a flush can always be forced by issuing Session.flush():"),
    ]
    db.session.add_all(post_list)
    db.session.add_all(comment_list)
    db.session.commit()

def undo_posts():
    db.session.execute('TRUNCATE comments RESTART IDENTITY CASCADE;')
    db.session.execute('TRUNCATE posts RESTART IDENTITY CASCADE;')
    db.session.commit()

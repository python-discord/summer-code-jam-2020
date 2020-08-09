# from django.shortcuts import render
from django.http import HttpResponse
# from django.contrib.auth.decorators import login_required
from dungeon.models.character import MudUser, Character
from django.views import View
from django.db import IntegrityError
from django.db.models import F


class CharacterView(View):
    def post(self, request):
        # Login Required
        # return HttpResponse("invalid") OR return HttpResponse("something")
        if request.user.is_authenticated:
            if request.POST["view_name"] == 'create_character':
                # create character
                # Parameter : name
                # return True : Success create character {name}
                # return Fail : invalid
                name = request.POST['name']
                user = MudUser.objects.get(pk=request.user.pk)
                character = Character(user=user, name=name)
                try:
                    character.save()
                except IntegrityError:
                    return HttpResponse("invalid")
                else:
                    return HttpResponse("Success create character " + name)
            elif request.POST["view_name"] == 'get_character_list':
                # character list of now Login user
                # Parameter : None
                # return True : name1,name2... | name1
                # return Fail : invalid
                user = MudUser.objects.get(pk=request.user.pk)
                character_name_list = []
                for obj in Character.objects.filter(user=user):
                    character_name_list.append(obj.name)
                if character_name_list:
                    return HttpResponse(",".join(character_name_list))
                else:
                    return HttpResponse("invalid")
            elif request.POST["view_name"] == 'get_character_stats':
                # character stats of now Login user
                # parameter : character_name (character of now Login user)
                # return True : hp : ~~ ..
                # return Fail : invalid
                user = MudUser.objects.get(pk=request.user.pk)
                character_name_list = []
                for obj in Character.objects.filter(user=user):
                    character_name_list.append(obj.name)
                if request.POST["character_name"] in character_name_list:
                    character_object = Character.objects.get(name=request.POST["character_name"])
                    return HttpResponse(character_object.name
                                        + " hp : "
                                        + str(character_object.hp)
                                        + "/"
                                        + str(character_object.max_hp)
                                        + " total attack : "
                                        + str(character_object.total_attack)
                                        + " attack cool time : "
                                        + str(character_object.attack_cool_time)
                                        + " total defense : "
                                        + str(character_object.total_defense))
                else:
                    return HttpResponse("invalid")
            elif request.POST["view_name"] == 'update_character_stats':
                # Update character stats of now Login user
                # parameter : character_name(character of now Login user), stats, num
                # return True : Success {stats_name} changed
                # return Fail : invalid
                user = MudUser.objects.get(pk=request.user.pk)
                character_name_list = []
                for obj in Character.objects.filter(user=user):
                    character_name_list.append(obj.name)
                if request.POST["character_name"] in character_name_list:
                    character_object = Character.objects.get(name=request.POST["character_name"])
                    if request.POST["stats"] == 'hp':
                        if character_object.hp == character_object.max_hp:
                            return HttpResponse("Success hp changed")
                        else:
                            character_object.hp = F('hp') + request.POST["num"]
                            character_object.save()
                        return HttpResponse("Success hp changed")
                    elif request.POST["stats"] == 'max_hp':
                        character_object.max_hp = F('max_hp') + request.POST["num"]
                        character_object.hp = F('hp') + request.POST["num"]
                        character_object.save()
                        return HttpResponse("Success max_hp changed")
                    elif request.POST["stats"] == 'attack_cool_time':
                        character_object.attack_cool_time = F('attack_cool_time') + request.POST["num"]
                        character_object.save()
                        return HttpResponse("Success attack cool time changed")
                    elif request.POST["stats"] == 'total_attack':
                        character_object.total_attack = F('total_attack') + request.POST["num"]
                        character_object.save()
                        return HttpResponse("Success total attack changed")
                    elif request.POST["stats"] == 'total_defense':
                        character_object.total_defense = F('total_defense') + request.POST["num"]
                        character_object.save()
                        return HttpResponse("Success total defense changed")
                    else:
                        return HttpResponse("invalid")
                else:
                    return HttpResponse("invalid")
            elif request.POST["view_name"] == 'select_character':
                # Select Character : enter a room
                # parameter : name (character_name(character of now Login user))
                # return True : Success Character Select {name}
                # return Fail : invalid
                user = MudUser.objects.get(pk=request.user.pk)
                character_name_list = []
                for obj in Character.objects.filter(user=user):
                    character_name_list.append(obj.name)
                if request.POST["name"] in character_name_list:
                    character_object = Character.objects.get(name=request.POST["name"])
                    user.now_connected_character_name = character_object.name
                    user.save()
                    return HttpResponse("Success Character Select " + request.POST["name"])
                else:
                    return HttpResponse("invalid")
            elif request.POST["view_name"] == 'get_userlist_in_room':
                # GET charater list in same room(with my character)
                # parameter : None
                # return True : name1,name2... | name1
                # return Fail : invalid
                user = MudUser.objects.get(pk=request.user.pk)
                if user.now_connected_character_name != '':
                    now_character = Character.objects.get(name=user.now_connected_character_name)
                    location_x = now_character.location_x
                    location_y = now_character.location_y
                    location_z = now_character.location_z
                    character_name_list = []
                    for obj in Character.objects.filter(location_x=location_x,
                                                        location_y=location_y,
                                                        location_z=location_z):
                        if obj.user.now_connected_character_name == obj.name:
                            character_name_list.append(obj.name)
                    return HttpResponse(",".join(character_name_list))
                else:
                    return HttpResponse("invalid")
            elif request.POST["view_name"] == 'attack_character':
                # attack # mycharacter -> others
                # parameter : target_user
                # return True : Success attack {target_user} -> Dead | hp : {number}
                # return Fail : return HttpResponse("invalid")
                user = MudUser.objects.get(pk=request.user.pk)
                if user.now_connected_character_name != '':
                    now_character = Character.objects.get(name=user.now_connected_character_name)
                    location_x = now_character.location_x
                    location_y = now_character.location_y
                    location_z = now_character.location_z
                    character_name_list = []
                    for obj in Character.objects.filter(location_x=location_x,
                                                        location_y=location_y,
                                                        location_z=location_z):
                        if obj.user.now_connected_character_name == obj.name:
                            character_name_list.append(obj.name)
                    # pytest.set_trace()
                    if request.POST["target_user"] in character_name_list and \
                            user.now_connected_character_name != request.POST["target_user"]:
                        attacker = Character.objects.get(name=user.now_connected_character_name)
                        target = Character.objects.get(name=request.POST["target_user"])
                        # Damage Formula : attack*(100/(100+defense))
                        target.hp = target.hp - attacker.total_attack*(100/(100+target.total_defense))
                        if target.hp <= 0:
                            target.hp = target.max_hp
                            target.location_x = 10
                            target.location_y = 10
                            target.location_z = 10
                            target.save()
                            message = "Success attack "+request.POST["target_user"] + " -> Dead"
                            return HttpResponse(message)
                        target.save()
                        target_hp = Character.objects.get(name=request.POST["target_user"]).hp
                        message = "Success attack "+request.POST["target_user"] + " -> hp : " + str(target_hp)
                        return HttpResponse(message)
                    else:
                        return HttpResponse("invalid")
                else:
                    return HttpResponse("invalid")
            else:
                return HttpResponse("invalid")
        else:
            return HttpResponse("invalid")
